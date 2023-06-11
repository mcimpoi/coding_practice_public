from collections import defaultdict
from copy import deepcopy
from bisect import bisect_right


class SnapshotArray:
    # for a given array -- we take snapshots (i.e. "copy" of the array values)
    # ops: get(index, snap_id)
    # set(index, val) --> don't modify the array directly;
    # if at snapshot snap_id there was no change on value at index,
    # get returns the value at the previous snapshot, or original value in the array

    # baseline impl:
    # in init, make a copy of the array, e.g. "dirty"
    # set --> apply changes to dirty
    # snap --> store dirty in array or map of snapshots

    #       get,  set, snap
    # Time: O(1), O(1), O(n)
    # Mem:  O(1), O(1), O(n) ; O(n^2) -- n snaps * n

    # we don't need to store all values; store only what changed (e.g. map)
    # worst case -- still store O(n) changes.
    # dirty --> now a dict; index: value
    # set --> dirty[index] = new_value;
    # snap --> self.snapshots[snap_id] = dirty // copy
    # get -- self.snapshots[snap_id] -- if it doesn't contain --> look for previous snaps
    # store self.modified[index] --> list of snapshot ids when the value was changed;
    # O(n) / O(logn) lookup

    # might not even need to store the array -- depending on possible values, e.g. sparse array

    def __init__(self, length: int):
        self.dirty = {}
        self.modified = defaultdict(list)  # index in array --> list of snapshot ids
        self.snapshot_id = 0
        self.snapshots = []  # list of dicts

    def set(self, index: int, val: int) -> None:
        self.dirty[index] = val
        if (
            len(self.modified[index]) == 0
            or self.modified[index][-1] != self.snapshot_id
        ):
            self.modified[index].append(self.snapshot_id)

    def snap(self) -> int:
        self.snapshots.append(deepcopy(self.dirty))
        self.dirty.clear()
        ret_val = self.snapshot_id
        self.snapshot_id += 1
        return ret_val

    def get(self, index: int, snap_id: int) -> int:
        idx = bisect_right(self.modified[index], snap_id)
        if idx > 0:
            return self.snapshots[self.modified[index][idx - 1]][index]
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

if __name__ == "__main__":
    # ["SnapshotArray","set","snap","set","get"]
    # [[3],[0,5],[],[0,6],[0,0]]
    snapshot_arr = SnapshotArray(3)
    snapshot_arr.set(0, 5)
    snapshot_arr.snap()
    snapshot_arr.set(0, 6)
    print(f"Actual: {snapshot_arr.get(0, 0)} Expected: 5")
