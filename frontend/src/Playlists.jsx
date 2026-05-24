import React from "react";

import PlaylistHeader from "./components/playlist/PlaylistHeader";
import PlaylistButtons from "./components/playlist/PlaylistButtons";
import PlaylistCard from "./components/playlist/PlaylistCard";
import VideoItem from "./components/playlist/VideoItem";

import useVideos from "./hooks/useVideos";
import useFlashcards from "./hooks/useFlashcards";
import useNotes from "./hooks/useNotes";

import {
  pageStyle,
  headerStyle,
  layoutGridStyle,
  sidebarStyle,
  contentStyle,
  cardStyle,
} from "./styles/playlistStyles";

export default function Playlists({

  playlists = [],

  selectedPlaylistId,

  setSelectedPlaylistId,

  refreshPlaylists,
}) {

  // =====================================
  // VIDEOS
  // =====================================

  const {

    videos,

    loading,

    loadVideos,
  } = useVideos();

  // =====================================
  // FLASHCARDS
  // =====================================

  const {

    flashcards,

    loadFlashcards,

    generateFlashcards,

    sendFlashcards,

    deleteFlashcard,
  } = useFlashcards();

  // =====================================
  // NOTES
  // =====================================

  const {

    openedNoteId,

    toggleNote,

    deleteNote,
  } = useNotes();

  // =====================================
  // PLAYLIST CLICK
  // =====================================

  const handlePlaylistClick = async (
    playlistId
  ) => {

    setSelectedPlaylistId(
      playlistId
    );

    await loadVideos(
      playlistId
    );
  };

  // =====================================
  // VIDEO ACTIONS
  // =====================================

  const handleOpenFlashcards = async (
    videoId
  ) => {

    await loadFlashcards(
      videoId
    );
  };

  const handleGenerateFlashcards =
    async (videoId) => {

      await generateFlashcards(
        videoId
      );

      await loadFlashcards(
        videoId
      );
    };

  const handleSendFlashcards =
    async (videoId) => {

      await sendFlashcards(
        videoId
      );
    };

  // =====================================
  // RENDER
  // =====================================

  return (

    <div style={pageStyle}>

      {/* ===================================== */}
      {/* HEADER */}
      {/* ===================================== */}

      <div style={headerStyle}>

        <PlaylistHeader />

        <PlaylistButtons
          refreshPlaylists={
            refreshPlaylists
          }
        />

      </div>

      {/* ===================================== */}
      {/* MAIN GRID */}
      {/* ===================================== */}

      <div style={layoutGridStyle}>

        {/* ===================================== */}
        {/* LEFT SIDEBAR */}
        {/* ===================================== */}

        <div style={sidebarStyle}>

          <div style={cardStyle}>

            <h2>
              Playlist List
            </h2>

            <div
              style={{
                marginTop: "14px",
                display: "flex",
                flexDirection:
                  "column",
                gap: "12px",
              }}
            >

              {playlists.map(
                (playlist) => (

                  <PlaylistCard
                    key={playlist.id}
                    playlist={
                      playlist
                    }
                    selected={
                      selectedPlaylistId ===
                      playlist.id
                    }
                    onClick={() =>
                      handlePlaylistClick(
                        playlist.id
                      )
                    }
                  />

                )
              )}

            </div>

          </div>

        </div>

        {/* ===================================== */}
        {/* CONTENT */}
        {/* ===================================== */}

        <div style={contentStyle}>

          <div style={cardStyle}>

            <h2>
              Playlist Videos
            </h2>

            {loading && (

              <div
                style={{
                  marginTop: "12px",
                }}
              >
                Loading...
              </div>
            )}

            {!loading &&
              videos.length === 0 && (

              <div
                style={{
                  marginTop: "12px",
                  opacity: 0.7,
                }}
              >
                Playlist seç.
              </div>
            )}

            <div
              style={{
                marginTop: "18px",
                display: "flex",
                flexDirection:
                  "column",
                gap: "14px",
              }}
            >

              {videos.map(
                (video) => (

                  <VideoItem
                    key={
                      video.video_id
                    }

                    video={video}

                    flashcards={
                      flashcards[
                        video.video_id
                      ] || []
                    }

                    openedNoteId={
                      openedNoteId
                    }

                    onToggleNote={() =>
                      toggleNote(
                        video.video_id
                      )
                    }

                    onDeleteNote={() =>
                      deleteNote(
                        video.video_id
                      )
                    }

                    onLoadFlashcards={() =>
                      handleOpenFlashcards(
                        video.video_id
                      )
                    }

                    onGenerateFlashcards={() =>
                      handleGenerateFlashcards(
                        video.video_id
                      )
                    }

                    onSendFlashcards={() =>
                      handleSendFlashcards(
                        video.video_id
                      )
                    }

                    onDeleteFlashcard={
                      deleteFlashcard
                    }
                  />

                )
              )}

            </div>

          </div>

        </div>

      </div>

    </div>
  );
}