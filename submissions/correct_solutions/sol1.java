import java.util.*;

///
/// Idea: Store the arrival times in an array
///       And keep a priority queue using a min heap to keep track of the smallest burst job
///       We keep pop elements out of the priority queue and move time by either
///       the total burst time, or by the arrival of a new job
///       The waiting time is calculated at the end, using the formula: current_time - arrival - burst
/// 

public class sol1 {

    public static void main(String[] args) {
        Scanner fs = new Scanner(System.in);
        int n = (int) fs.nextLong();
        long[] a = new long[n]; 
        long[] b = new long[n]; 
        long[] rem = new long[n];
        long sumM = 0;
        
        for (int i = 0; i < n; i++) {
            a[i] = fs.nextLong();   //arrival time
            b[i] = fs.nextLong();   //burst time
            sumM = (sumM + fs.nextLong()); //memory cost (added only once)
            rem[i] = b[i]; // time remaining
        }

        Integer[] byArrival = new Integer[n];
        for (int i = 0; i < n; i++) {
            byArrival[i] = i;
        }
        //sort the jobs by their respective arrival time
        Arrays.sort(byArrival, (x, y) -> Long.compare(a[x], a[y])); // NlogN time

        // min-heap of process ids sorted by remaining time
        PriorityQueue<Integer> heap = new PriorityQueue<>((x, y) -> Long.compare(rem[x], rem[y]));

        long t = 0; // time
        int p = 0; //job position
        long ans = 0;
        

        while (p < n || !heap.isEmpty()) { // main loop
            if (heap.isEmpty()) t = Math.max(t, a[byArrival[p]]);
            while (p < n && a[byArrival[p]] <= t) heap.add(byArrival[p++]);
            int cur = heap.poll(); //picks the jobs with the current smallest burst time
            long nextArrival = (p < n) ? a[byArrival[p]] : Long.MAX_VALUE;
            long run = Math.min(rem[cur], nextArrival - t); //how long this will run for (rem[cur]:current job execution, nextArrival-t:next job arrival)
            t += run ; //move time forward
            rem[cur] -= run ;

            if (rem[cur] == 0) {
                //job is fully executed, add the wait time
                ans = ans + (t - a[cur] - b[cur]);
            } else {
                heap.add(cur); // preempted by an arrival
            }
        }
        System.out.println(ans + sumM);
    }
}