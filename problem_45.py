from heapq import heappush, heappop

# Definition for an Interval.
class Interval:
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end

def employeeFreeTime(schedule):
    # Initialize a min-heap
    heap = []
    
    # Push the first interval of each employee onto the heap
    for emp_id, intervals in enumerate(schedule):
        if intervals:
            heappush(heap, (intervals[0].start, intervals[0].end, emp_id, 0))
    
    # This will store the merged intervals
    merged_intervals = []
    
    # Process the heap
    while heap:
        start, end, emp_id, interval_idx = heappop(heap)
        
        # If merged_intervals is empty or there's no overlap, add the interval
        if not merged_intervals or merged_intervals[-1].end < start:
            merged_intervals.append(Interval(start, end))
        else:
            # There's overlap, so merge the intervals
            merged_intervals[-1].end = max(merged_intervals[-1].end, end)
        
        # If there's a next interval for the same employee, push it onto the heap
        if interval_idx + 1 < len(schedule[emp_id]):
            next_interval = schedule[emp_id][interval_idx + 1]
            heappush(heap, (next_interval.start, next_interval.end, emp_id, interval_idx + 1))
    
    # Now, find the gaps between the merged intervals to get the free time
    free_times = []
    for i in range(1, len(merged_intervals)):
        prev_end = merged_intervals[i - 1].end
        curr_start = merged_intervals[i].start
        if prev_end < curr_start:
            free_times.append(Interval(prev_end, curr_start))
    
    return free_times

