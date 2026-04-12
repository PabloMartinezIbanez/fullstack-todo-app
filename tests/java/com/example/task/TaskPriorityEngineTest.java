package com.example.task;

public class TaskPriorityEngineTest {
    public static void main(String[] args) {
        shouldScoreOverdueHighPriorityHigher();
        shouldEscalateHighScoreTasks();
        shouldAssignUrgentQueueForOverdue();
    }

    private static void shouldScoreOverdueHighPriorityHigher() {
        int score = TaskPriorityEngine.computePriorityScore("high", true, 9, 8);
        assertEquals(90, score, "Overdue high-priority tasks should have a high score.");
    }

    private static void shouldEscalateHighScoreTasks() {
        boolean result = TaskPriorityEngine.needsEscalation("high", true, 9, 8);
        assertTrue(result, "High-score tasks should be escalated.");
    }

    private static void shouldAssignUrgentQueueForOverdue() {
        String queue = TaskPriorityEngine.assignQueue("low", true);
        assertEquals("urgent", queue, "Overdue tasks should use urgent queue.");
    }

    private static void assertEquals(int expected, int actual, String message) {
        if (expected != actual) {
            throw new AssertionError(message + " Expected " + expected + " but got " + actual + ".");
        }
    }

    private static void assertEquals(String expected, String actual, String message) {
        if (!expected.equals(actual)) {
            throw new AssertionError(message + " Expected " + expected + " but got " + actual + ".");
        }
    }

    private static void assertTrue(boolean value, String message) {
        if (!value) {
            throw new AssertionError(message);
        }
    }
}
