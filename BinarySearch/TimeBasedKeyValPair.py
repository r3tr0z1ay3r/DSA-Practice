"""
prblM:
->Implement a storage for multiple val at same timestamp 
->Retrive value from specified timestamp

->Fn set gets the key(Person),value(State),timestamp(time) and stores it and timestamp
-> Get fn returns the most recent available value, it takes timestamp as input,
    if timestamp is available in the storage, return that or find the next latest value(next min value),
    if there are no values in the given key, return emptystring
->All calls to set have timestamps in increasing order(ascending) (Clue for using binary serach)

Approach:
 -> Using the person as key store (State,timestamp) pair to each in set fn,

 -> In the get fn, check if the key exists in the map,if it exists fetch its values and store, if not return empty set
 -> Create a binary search to comparing the time of storage to the timestamp required and update return_value when lower.
 -> Search continues until we hit the timestamp or the most available before timestamp 
 -> Return the state at that timestamp

"""



class TimeMap:

    def __init__(self):
        self.keys = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key]= []
        self.keys[key].append([value,timestamp])


    def get(self, key: str, timestamp: int) -> str:
        mood,val = "",self.keys.get(key,[])
        l,r = 0,len(val)-1
        while l<= r:
            mid = l+(r-l)//2
            if val[mid][1] <= timestamp:
                mood = val[mid][0]
                l = mid +1
            else:
                r = mid - 1
        return mood
            

obj = TimeMap()

obj.set("alice","happy",1)
print(obj.get("alice",1))