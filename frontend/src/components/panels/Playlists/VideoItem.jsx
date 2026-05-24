import { useState } from "react";

import NotePanel from "./NotePanel";

import FlashcardPanel from "./FlashcardPanel";

import PlaylistButtons from "./PlaylistButtons";

export default function VideoItem({

  video,

  playlistId,

  selectedVideo,
  setSelectedVideo,
}) {

  // =====================================
  // STATES
  // =====================================

  const [showNotes, setShowNotes] =
    useState(false);

  const [
    showFlashcards,
    setShowFlashcards,
  ] = useState(false);

  // =====================================
  // SELECTED
  // =====================================

  const isSelected =
    selectedVideo ===
    video.video_id;

  // =====================================
  // RENDER
  // =====================================

  return (

    <div
      style={{
        background:
          isSelected
            ? "#202020"
            : "#151515",

        border:
          isSelected
            ? "1px solid lime"
            : "1px solid #2a2a2a",

        borderRadius:
          "14px",

        padding: "14px",

        marginBottom:
          "12px",
      }}
    >

      {/* HEADER */}

      <div
        style={{
          display: "flex",
          justifyContent:
            "space-between",
          gap: "12px",
        }}
      >

        <div
          style={{
            flex: 1,
          }}
        >

          <div
            style={{
              fontWeight:
                "bold",

              marginBottom:
                "8px",

              lineHeight:
                "1.4",
            }}
          >
            {video.title}
          </div>

          <div
            style={{
              opacity: 0.6,
              fontSize: "12px",
            }}
          >
            VIDEO ID:
            {" "}
            {video.video_id}
          </div>

        </div>

        <button
          onClick={() =>
            setSelectedVideo(
              video.video_id
            )
          }
          style={{
            background:
              isSelected
                ? "lime"
                : "#333",

            color:
              isSelected
                ? "black"
                : "white",

            border: "none",

            borderRadius:
              "8px",

            padding:
              "8px 12px",

            cursor: "pointer",

            fontWeight:
              "bold",

            height: "40px",
          }}
        >
          {isSelected
            ? "Selected"
            : "Select"}
        </button>

      </div>

      {/* BUTTONS */}

      <PlaylistButtons
        video={video}
        playlistId={playlistId}
        showNotes={showNotes}
        setShowNotes={
          setShowNotes
        }
        showFlashcards={
          showFlashcards
        }
        setShowFlashcards={
          setShowFlashcards
        }
      />

      {/* NOTES */}

      {showNotes && (

        <NotePanel
          videoId={
            video.video_id
          }
        />

      )}

      {/* FLASHCARDS */}

      {showFlashcards && (

        <FlashcardPanel
          videoId={
            video.video_id
          }
        />

      )}

    </div>
  );
}