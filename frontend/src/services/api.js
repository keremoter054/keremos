const API_BASE =
  "http://127.0.0.1:8000";

// =====================================
// ROOT
// =====================================

export async function getRoot() {

  const response =
    await fetch(`${API_BASE}/`);

  return await response.json();
}

// =====================================
// VIDEO HEALTH
// =====================================

export async function getVideoHealth() {

  const response =
    await fetch(
      `${API_BASE}/video/health`
    );

  return await response.json();
}

// =====================================
// VIDEO STATUS SUMMARY
// =====================================

export async function getVideoStatusSummary() {

  const response =
    await fetch(
      `${API_BASE}/video/status/summary`
    );

  return await response.json();
}

// =====================================
// VIDEO PROGRESS
// =====================================

export async function getVideoProgress(
  videoId
) {

  const response =
    await fetch(
      `${API_BASE}/video/progress/${videoId}`
    );

  return await response.json();
}

// =====================================
// VIDEO RESULT
// =====================================

export async function getVideoResult(
  videoId
) {

  const response =
    await fetch(
      `${API_BASE}/video/result/${videoId}`
    );

  return await response.json();
}

// =====================================
// START ANALYSIS
// =====================================

export async function startAnalysis(
  videoId
) {

  const response =
    await fetch(

      `${API_BASE}/video/analyze/start?video_id=${videoId}`,

      {
        method: "POST",
      }
    );

  return await response.json();
}