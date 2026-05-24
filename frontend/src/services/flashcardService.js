import { API } from "../config/config";

// =====================================
// GET FLASHCARDS
// =====================================

export async function getFlashcards(
  videoId
) {

  const res = await fetch(
    `${API}/flashcards/${videoId}`
  );

  if (!res.ok) {

    throw new Error(
      "Flashcard fetch failed"
    );
  }

  return await res.json();
}

// =====================================
// GENERATE FLASHCARDS
// =====================================

export async function generateFlashcards(
  videoId
) {

  const res = await fetch(
    `${API}/flashcards/generate/${videoId}`,
    {
      method: "POST",
    }
  );

  if (!res.ok) {

    throw new Error(
      "Flashcard generate failed"
    );
  }

  return await res.json();
}

// =====================================
// DELETE FLASHCARD
// =====================================

export async function deleteFlashcard(
  cardId
) {

  const res = await fetch(
    `${API}/flashcards/${cardId}`,
    {
      method: "DELETE",
    }
  );

  if (!res.ok) {

    throw new Error(
      "Flashcard delete failed"
    );
  }

  return await res.json();
}

// =====================================
// SEND ALL TO ANKI
// =====================================

export async function sendAllFlashcardsToAnki(
  videoId
) {

  const res = await fetch(
    `${API}/flashcards/send-all/${videoId}`,
    {
      method: "POST",
    }
  );

  if (!res.ok) {

    throw new Error(
      "Anki send failed"
    );
  }

  return await res.json();
}

// =====================================
// UPDATE FLASHCARD
// =====================================

export async function updateFlashcard(

  cardId,
  content

) {

  const res = await fetch(
    `${API}/flashcards/${cardId}`,
    {
      method: "PUT",

      headers: {
        "Content-Type":
          "application/json",
      },

      body: JSON.stringify({
        content,
      }),
    }
  );

  if (!res.ok) {

    throw new Error(
      "Flashcard update failed"
    );
  }

  return await res.json();
}