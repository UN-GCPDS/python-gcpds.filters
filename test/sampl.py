from gcpds.filters.spatial.masker import generate_mask
from gcpds.utils import loaddb


db = 'HighGamma_ME'
channels, montage_name = getattr(loaddb, db).metadata['channel_names'], getattr(
    loaddb, db).metadata['montage']

print(f"Channels: {channels}")
print(f"Montage: {montage_name}")

mask = generate_mask(channels, montage_name)
print(f"Mask: \n{mask}")
