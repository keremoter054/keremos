import { API } from "../config/config";

// =====================================
// GET FULL NOTES
// =====================================

export async function getFullNotes(
  videoId
) {

  const res = await fetch(
    `${API}/video/full-notes?video_id=${videoId}`
  );

  if (!res.ok) {

    throw new Error(
      "Note fetch failed"
    );
  }

  return await res.json();
}

// =====================================
// GENERATE VIDEO NOTES
// =====================================

export async function generateVideoNotes(
  videoId
) {

  const res = await fetch(
    `${API}/video/analyze/start?video_id=${videoId}`
  );

  if (!res.ok) {

    throw new Error(
      "Note generate failed"
    );
  }

  return await res.json();
}

// =====================================
// DELETE VIDEO NOTES
// =====================================

export async function deleteVideoNotes(
  videoId
) {

  const res = await fetch(
    `${API}/notes/${videoId}`,
    {
      method: "DELETE",
    }
  );

  if (!res.ok) {

    throw new Error(
      "Note delete failed"
    );
  }

  return await res.json();
}

// =====================================
// GET VIDEO PROGRESS
// =====================================

export async function getVideoProgress(
  videoId
) {

  const res = await fetch(
    `${API}/video/progress?video_id=${videoId}`
  );

  if (!res.ok) {

    throw new Error(
      "Video progress fetch failed"
    );
  }

  return await res.json();
}

// =====================================
// OPEN HTML NOTES PAGE
// =====================================

export function openNotesPage(
  videoId
) {

  window.open(

    `${API}/video/full-notes/view?video_id=${videoId}`,

    "_blank"
  );
}