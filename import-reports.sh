#!/bin/bash
DBCLIPATH="/usr/local/bin"
BUNDLETARGET=""dev""
JQPATH="/usr/bin"

DATABRICKS_BUNDLE_WORKSPACE_ROOT_PATH=""
getPath="${DBCLIPATH}/databricks bundle validate -t ${BUNDLETARGET} | ${JQPATH}/jq -r .workspace.file_path"
output="sh(script: getPath, returnStdout: true).trim()"
echo $output
