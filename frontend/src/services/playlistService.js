import { API } from "../config/config";

// =====================================
// FETCH PLAYLISTS
// =====================================

export async function fetchPlaylists() {

  const res = await fetch(
    `${API}/playlists`
  );

  if (!res.ok) {

    throw new Error(
      "Playlist fetch failed"
    );
  }

  return await res.json();
}

// =====================================
// FETCH PLAYLIST VIDEOS
// =====================================

export async function fetchPlaylistVideos(
  playlistId
) {

  const res = await fetch(
    `${API}/playlist/${playlistId}/videos`
  );

  if (!res.ok) {

    throw new Error(
      "Video fetch failed"
    );
  }

  return await res.json();
}

// =====================================
// IMPORT PLAYLIST
// =====================================

export async function importPlaylist({

  playlist_url,
  category,

}) {

  const res = await fetch(
    `${API}/playlists/import`,
    {
      method: "POST",

      headers: {
        "Content-Type":
          "application/json",
      },

      body: JSON.stringify({

        playlist_url,
        category,
      }),
    }
  );

  if (!res.ok) {

    throw new Error(
      "Playlist import failed"
    );
  }

  return await res.json();
}

// =====================================
// REORDER PLAYLISTS
// =====================================

export async function reorderPlaylists(
  order
) {

  const res = await fetch(
    `${API}/playlists/reorder`,
    {
      method: "POST",

      headers: {
        "Content-Type":
          "application/json",
      },

      body: JSON.stringify({
        order,
      }),
    }
  );

  if (!res.ok) {

    throw new Error(
      "Playlist reorder failed"
    );
  }

  return await res.json();
}

// =====================================
// GLOBAL ESTIMATE
// =====================================

export async function fetchGlobalEstimate() {

  const res = await fetch(
    `${API}/global-estimate`
  );

  if (!res.ok) {

    throw new Error(
      "Global estimate fetch failed"
    );
  }

  return await res.json();
}

// =====================================
// VIDEO STATUS SUMMARY
// =====================================

export async function fetchVideoStatusSummary() {

  const res = await fetch(
    `${API}/videos/status/summary`
  );

  if (!res.ok) {

    throw new Error(
      "Video summary fetch failed"
    );
  }

  return await res.json();
}