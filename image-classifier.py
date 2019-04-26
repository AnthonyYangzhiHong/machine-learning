import numpy as np
import matplotlib.pyplot as plt
import gzip, struct

file_name = 't10k-images-idx3-ubyte.gz'

with gzip.open(file_name) as f:
	f.read(4)
	f.read(4)
	f.read(4)
	f.read(4)

	buf = f.read(28*28)

	image = np.frombuffer(buf, dtype=np.uint8)

	print("Pixels", image[:10])

_, (ax1, ax2) = plt.subplots(1,2)

ax1.imshow(image.reshape(28,28), cmap=plt.cm.Greys);
ax2.hist(image, bins=20, range=[0,255]);

plt.show()
