# Copyright (c) 2013 Spotify AB
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

from .annoylib import *

class AnnoyIndex(Annoy):
    # This class is a dummy wrapper around the underlying C++ class.
    # The plan is to remove it soon.
    def add_item(self, i, vector):
        """
        Adds item `i` (any nonnegative integer) with vector `v`.

        Note that it will allocate memory for `max(i)+1` items.
        """
        return super(AnnoyIndex, self).add_item(i, vector)

    def get_nns_by_item(self, i, n, search_k=-1, include_distances=False):
        """
        Returns the `n` closest items to item `i`.

        :param search_k: the query will inspect up to `search_k` nodes.
        `search_k` gives you a run-time tradeoff between better accuracy and speed.
        `search_k` defaults to `n_trees * n` if not provided.

        :param include_distances: If `True`, this function will return a
        2 element tuple of lists. The first list contains the `n` closest items.
        The second list contains the corresponding distances.
        """
        # Wrapper to support named arguments
        return super(AnnoyIndex, self).get_nns_by_item(i, n, search_k, include_distances)

    def get_item_vector(self, i):
        """
        Returns the vector for item `i` that was previously added.
        """
        return super(AnnoyIndex, self).get_item_vector(i)

    def get_distance(self, i, j):
        """
        Returns the distance between items `i` and `j`.
        """
        return super(AnnoyIndex, self).get_distance(i, j)
