import numpy as np


def ascent():
    """
    Get an 8-bit grayscale bit-depth, 512 x 512 derived image for
    easy use in demos

    The image is derived from accent-to-the-top.jpg at
    http://www.public-domain-image.com/people-public-domain-images-pictures/

    Parameters
    ----------
    None

    Returns
    -------
    ascent : ndarray
       convenient image to use for testing and demonstration

    Examples
    --------
    >>> import pywt.misc
    >>> ascent = pywt.misc.ascent()
    >>> ascent.shape
    (512, 512)
    >>> ascent.max()
    255

    >>> import matplotlib.pyplot as plt
    >>> plt.gray()
    >>> plt.imshow(ascent)
    >>> plt.show()

    """
    import pickle
    import os
    fname = os.path.join(os.path.dirname(__file__), 'ascent.dat')
    with open(fname, 'rb') as f:
        ascent = np.array(pickle.load(f))
    return ascent


def face(gray=False):
    """
    Get a 1024 x 768, color image of a raccoon face.

    raccoon-procyon-lotor.jpg at http://www.public-domain-image.com

    Parameters
    ----------
    gray : bool, optional
        If True then return color image, otherwise return an 8-bit gray-scale

    Returns
    -------
    face : ndarray
        image of a racoon face

    Examples
    --------
    >>> import pywt.misc
    >>> face = pywt.misc.face()
    >>> face.shape
    (768, 1024, 3)
    >>> face.max()
    255
    >>> face.dtype
    dtype('uint8')

    >>> import matplotlib.pyplot as plt
    >>> plt.gray()
    >>> plt.imshow(face)
    >>> plt.show()

    """
    import bz2
    import os
    with open(os.path.join(os.path.dirname(__file__), 'face.dat'), 'rb') as f:
        rawdata = f.read()
    data = bz2.decompress(rawdata)
    face = np.fromstring(data, dtype='uint8')
    face.shape = (768, 1024, 3)
    if gray is True:
        face = (0.21 * face[:, :, 0]
                + 0.71 * face[:, :, 1]
                + 0.07 * face[:, :, 2]).astype('uint8')
    return face


def aero():
    """
    Get an 8-bit grayscale bit-depth, 512 x 512 derived image for
    easy use in demos

    Parameters
    ----------
    None

    Returns
    -------
    aero : ndarray
       convenient image to use for testing and demonstration

    Examples
    --------
    >>> import pywt.misc
    >>> aero = pywt.misc.ascent()
    >>> aero.shape
    (512, 512)
    >>> aero.max()
    255

    >>> import matplotlib.pyplot as plt
    >>> plt.gray()
    >>> plt.imshow(aero)
    >>> plt.show()

    """
    import os
    fname = os.path.join(os.path.dirname(__file__), 'aero.dat')
    with open(fname, 'rb') as f:
        aero = np.load(f)
    return aero
