// =====================================
// IMPORTS
// =====================================

import {
  colors,
} from "./theme";

// =====================================
// MAIN CARD
// =====================================

export const cardStyle = {

  background:
    colors.card,

  padding: "18px",

  borderRadius: "16px",

  border:
    `1px solid ${colors.border}`,
};

// =====================================
// SECONDARY CARD
// =====================================

export const secondaryCardStyle = {

  background:
    colors.cardSecondary,

  padding: "14px",

  borderRadius: "12px",

  border:
    `1px solid ${colors.border}`,
};

// =====================================
// SELECTED CARD
// =====================================

export const selectedCardStyle = {

  background:
    "#2a2a2a",

  border:
    `1px solid ${colors.success}`,
};

// =====================================
// HOVER CARD
// =====================================

export const hoverCardStyle = {

  transition:
    "0.2s ease",

  cursor: "pointer",
};

// =====================================
// PANEL CARD
// =====================================

export const panelCardStyle = {

  display: "flex",

  flexDirection:
    "column",

  gap: "20px",
};

// =====================================
// STATUS CARD
// =====================================

export const statusCardStyle = {

  minWidth: "220px",
};

// =====================================
// TASK CARD
// =====================================

export const taskCardStyle = {

  background:
    "#222",

  padding: "15px",

  borderRadius: "10px",

  border:
    `1px solid ${colors.border}`,
};

// =====================================
// ACTIVE TASK CARD
// =====================================

export const activeTaskCardStyle = {

  background:
    "#333",

  border:
    `1px solid ${colors.success}`,
};

// =====================================
// TIMELINE DAY CARD
// =====================================

export const timelineDayCardStyle = {

  background:
    colors.cardSecondary,

  padding: "15px",

  borderRadius: "12px",

  cursor: "pointer",

  border:
    `1px solid ${colors.border}`,
};

// =====================================
// ACTIVE TIMELINE DAY CARD
// =====================================

export const activeTimelineDayCardStyle = {

  background:
    "#2f2f2f",

  border:
    `1px solid ${colors.success}`,
};