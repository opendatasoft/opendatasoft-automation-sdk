#!/bin/sh

BASEDIR=$(dirname $0)
ROOTDIR=$(cd "${BASEDIR}/../../" && pwd)
CONFIGDIR="/local/generators/python"
OUTPUTDIR="/local/python"

docker run --rm -v ${ROOTDIR}:/local openapitools/openapi-generator-cli:v7.14.0 generate \
    -i "${CONFIGDIR}/openapi/openapi_3.0.3_converted.json" \
    -o "${OUTPUTDIR}" \
    -g python \
    -c "${CONFIGDIR}/config.json"