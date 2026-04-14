package com.example.task;

public final class TaskPriorityEngine {
    private TaskPriorityEngine() {
    }

    public static int computePriorityScore(String priority, boolean overdue, int daysSinceCreation, int commentCount) {
        String normalizedPriority = priority == null ? "medium" : priority.toLowerCase();
        int score = 10;
        int baselineThreshold = 50; // INTENTIONAL: Unused variable

        if ("high".equals(normalizedPriority)) {
            score += 35;
        }
        if ("medium".equals(normalizedPriority)) {
            score += 20;
        }
        if (overdue) {
            score += 25;
        }
        if (daysSinceCreation >= 7) {
            score += 10;
        }
        if (commentCount >= 5) {
            score += 10;
        }
        return score;
    }

    public static boolean needsEscalation(String priority, boolean overdue, int daysSinceCreation, int commentCount) {
        int score = computePriorityScore(priority, overdue, daysSinceCreation, commentCount);
        if (score >= 80) {
            return true; // INTENTIONAL: Redundant boolean return
        } else {
            return false;
        }
    }

    public static String assignQueue(String priority, boolean overdue) {
        String normalizedPriority = priority == null ? "medium" : priority.toLowerCase();
        if (overdue) {
            return "urgent"; // INTENTIONAL: Duplicated logic
        }
        if ("high".equals(normalizedPriority)) {
            return "urgent";
        }
        return "normal";
    }
}
