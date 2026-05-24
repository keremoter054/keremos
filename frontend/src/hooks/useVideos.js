import { useState } from "react";

import {

  fetchPlaylistVideos,

} from "../services/playlistService";

export default function useVideos() {

  // =====================================
  // STATES
  // =====================================

  const [videosMap, setVideosMap] =
    useState({});

  const [openPlaylistId, setOpenPlaylistId] =
    useState(null);

  const [selectedVideo, setSelectedVideo] =
    useState(null);

  const [loadingVideos, setLoadingVideos] =
    useState(false);

  // =====================================
  // LOAD VIDEOS
  // =====================================

  const loadVideos = async (
    playlistId
  ) => {

    try {

      setLoadingVideos(true);

      const data =
        await fetchPlaylistVideos(
          playlistId
        );

      setVideosMap((prev) => ({

        ...prev,

        [playlistId]:
          Array.isArray(data)
            ? data
            : [],
      }));

    } catch (err) {

      console.error(
        "VIDEO LOAD ERROR:",
        err
      );

    } finally {

      setLoadingVideos(false);
    }
  };

  // =====================================
  // TOGGLE PLAYLIST
  // =====================================

  const togglePlaylist =
    async (playlistId) => {

      if (
        openPlaylistId ===
        playlistId
      ) {

        setOpenPlaylistId(null);

        return;
      }

      setOpenPlaylistId(
        playlistId
      );

      // cache kontrol
      if (
        !videosMap[
          playlistId
        ]
      ) {

        await loadVideos(
          playlistId
        );
      }
    };

  // =====================================
  // RETURN
  // =====================================

  return {

    videosMap,

    setVideosMap,

    openPlaylistId,
    setOpenPlaylistId,

    selectedVideo,
    setSelectedVideo,

    loadingVideos,

    loadVideos,
    togglePlaylist,
  };
}