import java.util.*;

class MutableInteger {
    private int value;
    public synchronized void increment() {
        value++;
    }
    public synchronized int getValue() {
        return value;
    }
}

class IncrementingRunnable implements Runnable {
    private final MutableInteger mutableInteger;
    public IncrementingRunnable(MutableInteger mutableInteger) {
        this.mutableInteger = mutableInteger;
    }

    @Override
    public void run() {
        for (int i = 0; i < 10000; i++) {
            mutableInteger.increment();
        }
    }
}

public class ThreadMain {
    public static void main (String[] args) {
        List<Thread> threads = new ArrayList<Thread>();

        MutableInteger integer = new MutableInteger();

        for (int i = 0; i < 10; i++) {
            Thread thread = new Thread(new IncrementingRunnable(integer));
            thread.start();
            threads.add(thread);
        }
        for (Thread thread : threads) {
           try {
           thread.join();
           } catch (InterruptedException e) {
               e.printStackTrace();
           }

           //thread.join();
        }

        System.out.println("Result value: " + integer.getValue());
    }
}

