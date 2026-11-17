import java.util.*;

public class sol1 {

    public static void main(String[] args) {
        Scanner fs = new Scanner(System.in);
        int n = (int) fs.nextLong();
        long[] a = new long[n]; 
        long[] b = new long[n]; 
        long[] rem = new long[n];
        long sumM = 0;
        
        for (int i = 0; i < n; i++) {
            a[i] = fs.nextLong();
            b[i] = fs.nextLong();
            sumM = (sumM + fs.nextLong());
            rem[i] = b[i]; // time remaining
        }

        Integer[] byArrival = new Integer[n];
        for (int i = 0; i < n; i++) {
            byArrival[i] = i;
        }
        Arrays.sort(byArrival, (x, y) -> Long.compare(a[x], a[y])); // NlogN time

        // min-heap of process ids sorted by remaining time
        PriorityQueue<Integer> heap = new PriorityQueue<>((x, y) -> Long.compare(rem[x], rem[y]));

        long t = 0, ans = 0;
        int p = 0;

        while (p < n || !heap.isEmpty()) { // main loop
            if (heap.isEmpty()) t = Math.max(t, a[byArrival[p]]);
            while (p < n && a[byArrival[p]] <= t) heap.add(byArrival[p++]);
            int cur = heap.poll();
            long nextArrival = (p < n) ? a[byArrival[p]] : Long.MAX_VALUE;
            long run = Math.min(rem[cur], nextArrival - t);
            t += run ;
            rem[cur] -= run ;

            if (rem[cur] == 0) {
                ans = ans + (t - a[cur] - b[cur]);
            } else {
                heap.add(cur); // preempted by an arrival
            }
        }
        System.out.println(ans + sumM);
    }
}