package com.example.task;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class TaskPriorityEngineTest {

    @Test
    public void shouldScoreOverdueHighPriorityHigher() {
        int score = TaskPriorityEngine.computePriorityScore("high", true, 9, 8);
        assertEquals(90, score, "Overdue high-priority tasks should have a high score.");
    }

    @Test
    public void shouldEscalateHighScoreTasks() {
        boolean result = TaskPriorityEngine.needsEscalation("high", true, 9, 8);
        assertTrue(result, "High-score tasks should be escalated.");
    }

    @Test
    public void shouldAssignUrgentQueueForOverdue() {
        String queue = TaskPriorityEngine.assignQueue("low", true);
        assertEquals("urgent", queue, "Overdue tasks should use urgent queue.");
    }
}
