import { useEffect, useState } from "react";

import {

  generateFlashcards,
  getFlashcards,

  deleteFlashcard,
  sendAllFlashcardsToAnki,

} from "../../services/flashcardService";

export default function FlashcardPanel({

  videoId,
}) {

  // =====================================
  // STATES
  // =====================================

  const [cards, setCards] =
    useState([]);

  const [loading, setLoading] =
    useState(false);

  const [status, setStatus] =
    useState("");

  // =====================================
  // LOAD
  // =====================================

  useEffect(() => {

    loadCards();

  }, [videoId]);

  // =====================================
  // LOAD CARDS
  // =====================================

  const loadCards = async () => {

    try {

      const data =
        await getFlashcards(
          videoId
        );

      setCards(
        data.cards || []
      );

    } catch (err) {

      console.error(
        "FLASHCARD LOAD ERROR:",
        err
      );
    }
  };

  // =====================================
  // GENERATE
  // =====================================

  const handleGenerate =
    async () => {

      try {

        setLoading(true);

        setStatus(
          "Generating..."
        );

        await generateFlashcards(
          videoId
        );

        await loadCards();

        setStatus(
          "Generated"
        );

      } catch (err) {

        console.error(
          "FLASHCARD GENERATE ERROR:",
          err
        );

        setStatus(
          "Generate Error"
        );

      } finally {

        setLoading(false);
      }
    };

  // =====================================
  // DELETE
  // =====================================

  const handleDelete =
    async (cardId) => {

      try {

        await deleteFlashcard(
          cardId
        );

        await loadCards();

      } catch (err) {

        console.error(
          "FLASHCARD DELETE ERROR:",
          err
        );
      }
    };

  // =====================================
  // SEND TO ANKI
  // =====================================

  const handleSendToAnki =
    async () => {

      try {

        setLoading(true);

        setStatus(
          "Sending To Anki..."
        );

        await sendAllFlashcardsToAnki(
          videoId
        );

        setStatus(
          "Sent To Anki"
        );

      } catch (err) {

        console.error(
          "ANKI SEND ERROR:",
          err
        );

        setStatus(
          "Anki Error"
        );

      } finally {

        setLoading(false);
      }
    };

  // =====================================
  // RENDER
  // =====================================

  return (

    <div
      style={{
        marginTop: "16px",

        background:
          "#111",

        border:
          "1px solid #2a2a2a",

        borderRadius:
          "12px",

        padding: "14px",
      }}
    >

      {/* HEADER */}

      <div
        style={{
          display: "flex",
          justifyContent:
            "space-between",

          alignItems:
            "center",

          marginBottom:
            "14px",
        }}
      >

        <div
          style={{
            fontWeight:
              "bold",

            fontSize:
              "16px",
          }}
        >
          Flashcards
        </div>

        <div
          style={{
            opacity: 0.7,
            fontSize: "12px",
          }}
        >
          {cards.length}
          {" "}
          cards
        </div>

      </div>

      {/* BUTTONS */}

      <div
        style={{
          display: "flex",
          gap: "10px",

          marginBottom:
            "14px",
        }}
      >

        <button
          onClick={
            handleGenerate
          }
          disabled={loading}
          style={{
            flex: 1,

            background:
              "lime",

            color: "black",

            border: "none",

            borderRadius:
              "8px",

            padding:
              "10px",

            cursor:
              "pointer",

            fontWeight:
              "bold",
          }}
        >
          Generate
        </button>

        <button
          onClick={
            handleSendToAnki
          }
          disabled={loading}
          style={{
            flex: 1,

            background:
              "#00d4ff",

            color: "black",

            border: "none",

            borderRadius:
              "8px",

            padding:
              "10px",

            cursor:
              "pointer",

            fontWeight:
              "bold",
          }}
        >
          Send Anki
        </button>

      </div>

      {/* STATUS */}

      {status && (

        <div
          style={{
            marginBottom:
              "14px",

            opacity: 0.8,

            fontSize:
              "13px",
          }}
        >
          {status}
        </div>

      )}

      {/* EMPTY */}

      {cards.length === 0 && (

        <div
          style={{
            opacity: 0.6,
            fontSize: "13px",
          }}
        >
          Flashcard yok.
        </div>

      )}

      {/* CARDS */}

      {cards.map((card) => (

        <div
          key={card.id}
          style={{
            background:
              "#1a1a1a",

            border:
              "1px solid #2f2f2f",

            borderRadius:
              "10px",

            padding:
              "12px",

            marginBottom:
              "10px",
          }}
        >

          <div
            style={{
              lineHeight:
                "1.5",

              marginBottom:
                "10px",
            }}
          >
            {card.content}
          </div>

          <div
            style={{
              display: "flex",
              justifyContent:
                "space-between",

              alignItems:
                "center",
            }}
          >

            <div
              style={{
                fontSize:
                  "12px",

                opacity: 0.6,
              }}
            >
              STATUS:
              {" "}
              {card.status}
            </div>

            <button
              onClick={() =>
                handleDelete(
                  card.id
                )
              }
              style={{
                background:
                  "red",

                color:
                  "white",

                border:
                  "none",

                borderRadius:
                  "6px",

                padding:
                  "6px 10px",

                cursor:
                  "pointer",
              }}
            >
              Sil
            </button>

          </div>

        </div>

      ))}

    </div>
  );
}