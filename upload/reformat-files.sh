#!/bin/bash
sed 's/\"\(.*\)\",.*,\(.*\),\(.*\),.*,.*,.*,\"\(.*\)\",\"\(.*\)\",\"\(.*\)\"/"\1",\2,\3,"\4\5\6"/'
