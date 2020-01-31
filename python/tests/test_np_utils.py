"""Numpy Protobuf utility tests"""

import numpy as np
import pytest

from xain_proto.np import ndarray_to_proto, proto_to_ndarray
from xain_proto.np.ndarray_pb2 import NDArray


@pytest.mark.parametrize(
    "numpy_array",
    [
        np.arange(10),
        np.arange(15).reshape(3, 5),
        np.array([1.2, 3.5, 5.1]),
        np.array([[1, 2], [3, 4]], dtype=complex),
        np.zeros((3, 4)),
        np.ones((2, 3, 4), dtype=np.int16),
    ],
)
def test_numpy_to_proto_to_numpy(numpy_array: np.ndarray) -> None:
    """Tests serialization and deserialization of numpy arrays.
    
    Args:
        numpy_array: A numpy array to serialize.
    """

    serialized_array: NDArray = ndarray_to_proto(numpy_array=numpy_array)
    deserialized_array: np.ndarray = proto_to_ndarray(proto_array=serialized_array)
    assert np.array_equal(numpy_array, deserialized_array)
