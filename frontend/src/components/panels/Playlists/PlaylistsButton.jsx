import {

  generateVideoNotes,

} from "../../services/noteService";

import {

  generateFlashcards,

  sendAllFlashcardsToAnki,

} from "../../services/flashcardService";

export default function PlaylistButtons({

  video,

  playlistId,

  showNotes,
  setShowNotes,

  showFlashcards,
  setShowFlashcards,
}) {

  // =====================================
  // GENERATE NOTES
  // =====================================

  const handleGenerateNotes =
    async () => {

      try {

        await generateVideoNotes(
          video.video_id
        );

        alert(
          "Note generation started"
        );

      } catch (err) {

        console.error(
          "NOTE GENERATE ERROR:",
          err
        );
      }
    };

  // =====================================
  // GENERATE FLASHCARDS
  // =====================================

  const handleGenerateFlashcards =
    async () => {

      try {

        await generateFlashcards(
          video.video_id
        );

        alert(
          "Flashcards generated"
        );

      } catch (err) {

        console.error(
          "FLASHCARD GENERATE ERROR:",
          err
        );
      }
    };

  // =====================================
  // SEND ANKI
  // =====================================

  const handleSendAnki =
    async () => {

      try {

        await sendAllFlashcardsToAnki(
          video.video_id
        );

        alert(
          "Sent to Anki"
        );

      } catch (err) {

        console.error(
          "ANKI SEND ERROR:",
          err
        );
      }
    };

  // =====================================
  // BUTTON STYLE
  // =====================================

  const buttonStyle = {

    flex: 1,

    border: "none",

    borderRadius:
      "8px",

    padding:
      "10px 12px",

    cursor:
      "pointer",

    fontWeight:
      "bold",
  };

  // =====================================
  // RENDER
  // =====================================

  return (

    <div
      style={{
        display: "grid",

        gridTemplateColumns:
          "repeat(2,1fr)",

        gap: "10px",

        marginTop:
          "16px",
      }}
    >

      {/* GENERATE NOTE */}

      <button
        onClick={
          handleGenerateNotes
        }
        style={{
          ...buttonStyle,

          background:
            "#00d4ff",

          color: "black",
        }}
      >
        Generate Note
      </button>

      {/* TOGGLE NOTES */}

      <button
        onClick={() =>
          setShowNotes(
            !showNotes
          )
        }
        style={{
          ...buttonStyle,

          background:
            showNotes
              ? "lime"
              : "#2a2a2a",

          color:
            showNotes
              ? "black"
              : "white",
        }}
      >
        {showNotes
          ? "Hide Notes"
          : "Show Notes"}
      </button>

      {/* GENERATE FLASHCARDS */}

      <button
        onClick={
          handleGenerateFlashcards
        }
        style={{
          ...buttonStyle,

          background:
            "#facc15",

          color: "black",
        }}
      >
        Generate Cards
      </button>

      {/* TOGGLE FLASHCARDS */}

      <button
        onClick={() =>
          setShowFlashcards(
            !showFlashcards
          )
        }
        style={{
          ...buttonStyle,

          background:
            showFlashcards
              ? "lime"
              : "#2a2a2a",

          color:
            showFlashcards
              ? "black"
              : "white",
        }}
      >
        {showFlashcards
          ? "Hide Cards"
          : "Show Cards"}
      </button>

      {/* SEND TO ANKI */}

      <button
        onClick={
          handleSendAnki
        }
        style={{
          ...buttonStyle,

          background:
            "lime",

          color: "black",

          gridColumn:
            "1 / span 2",
        }}
      >
        Send All To Anki
      </button>

    </div>
  );
}