# garbage_patch_kids

## Environment:
- [Install OceanParcels](http://oceanparcels.org/#installing-parcels)

## Data:
- source: http://ncss.hycom.org/thredds/ncss/grid/GLBu0.08/expt_91.2/uv3z/dataset.html
- `ncdump -h <filename>.nc` to get data headers
- `*.nc` files are gitignored because they're too big, zipped files are commited instead

## Tooling:
- `*.nc` to `.json`: https://github.com/jllodra/ncdump-json
