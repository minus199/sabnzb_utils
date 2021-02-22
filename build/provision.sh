CONTAINER="sabnzbd"
set -e
COMMON_MODULES_PATH_SRC=$(realpath $(dirname "$0")/../common)
COMMON_MODULES_PATH_DEST="/xmodules"

PROV_CHK_PNT="/app/provisoned.chkpnt"
if docker exec "${CONTAINER}" sh -c "test -f ${PROV_CHK_PNT} && echo 'Already provisioned.'"; then
    exit 0
fi

echo "Creating root common directory..."
docker exec "${CONTAINER}" sh -c "mkdir -p $COMMON_MODULES_PATH_DEST && chown abc:abc $COMMON_MODULES_PATH_DEST"

echo "Installing python deps on ${CONTAINER}..."
docker exec "${CONTAINER}" /usr/bin/python3 -m pip install --upgrade pip
docker exec "${CONTAINER}" /usr/bin/python3 -m pip install setuptools
docker exec "${CONTAINER}" /usr/bin/python3 -m pip install subliminal ipython

echo "Copying from ${COMMON_MODULES_PATH_SRC} to ${CONTAINER}:${COMMON_MODULES_PATH_DEST}..."
docker cp "${COMMON_MODULES_PATH_SRC}" "${CONTAINER}:${COMMON_MODULES_PATH_DEST}/"

echo "Adding ${COMMON_MODULES_PATH_DEST} to python path"

if docker exec "${CONTAINER}" sh -c "test -z '${PYTHONPATH}'"; then
    docker exec "${CONTAINER}" sh -c "echo export PYTHONPATH='${COMMON_MODULES_PATH_DEST}/' >> ~/.bashrc"
else
    docker exec "${CONTAINER}" sh -c "echo export PYTHONPATH='${PYTHONPATH}:${COMMON_MODULES_PATH_DEST}/' >> ~/.bashrc"
fi

docker exec "${CONTAINER}" touch $PROV_CHK_PNT