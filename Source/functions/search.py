__author__ = 'Andre'

import os
import time
import sys

from whoosh import analysis, fields, index
from whoosh.lang.stopwords import stoplists
from whoosh.util import now
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.index import open_dir
from whoosh.qparser import QueryParser

sourcedir = str("C:/Users/Andre")
indexdir = 'index'

ana = analysis.StemmingAnalyzer(stoplist=stoplists["en"], maxsize=40)

class PydocSchema(fields.SchemaClass):

    path = fields.STORED
    title = fields.TEXT(stored=True, sortable=True, spelling=True, analyzer=ana)
    tgrams = fields.NGRAMWORDS
    ext = fields.TEXT(stored=True, sortable=True)
    content = fields.TEXT(spelling=True, analyzer=ana)
    chapter = fields.ID(sortable=True)
    size = fields.NUMERIC(sortable=True)
    lastopened = fields.TEXT(sortable=True)
    lastchanged = fields.TEXT(sortable=True)
    created = fields.TEXT(sortable=True)

ix = index.create_in(indexdir, PydocSchema)
with ix.writer(limitmb=2048) as w:
    t = now()
    for dirpath, dirnames, filenames in os.walk(sourcedir):
        try:
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                size = os.path.getsize(filepath)

                path = dirpath
                chapter = unicode(os.path.basename(dirpath))
                fileName, fileExt = os.path.splitext(filename)
                fileName = unicode(fileName)
                fileExt = unicode(fileExt)
                data = None

                print dirpath, filename
                try:
                    lasto = time.ctime(os.stat(filepath).st_atime)
                    lasto = unicode(lasto[4:])

                    lasta = time.ctime(os.stat(filepath).st_mtime)
                    lasta = unicode(lasta[4:])

                    created = time.ctime(os.stat(filepath).st_ctime)
                    created = unicode(created[4:])

                    w.add_document(path=path,
                                    title=fileName, tgrams=fileName,
                                    ext=fileExt,
                                    content=data,
                                    chapter=chapter,
                                    size=size,
                                    lastopened=lasto,
                                    lastchanged=lasta,
                                    created=created)
                    print "-", now() - t
                except:
                    IndentationError
        except:
            UnicodeDecodeError
    print now() -t
print now() - t
test = open_dir('index')
print test.schema
results = ix.searcher().documents()
count = 0
qp= QueryParser("title", schema=test.schema)
q = qp.parse("AlbumArtSmall")
print "begin with search", now()- t
with ix.searcher() as s:
    toppie = s.search(q, limit=None)
    matching_ids = []
    for result in toppie:
        count += 1
        print count, result['title'], result['path']
        print now() - t
print "done"

