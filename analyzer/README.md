# Analyzer


📜 **Code Complexity Analyzer: Because Why Not?**

  *"Measuring code complexity with an arbitrary scale—because...it's umm...scientific?"

🛠 **What is the Code Complexity Analyzer?**

The Code Complexity Analyzer is an experimental tool designed to give Python scripts a "complexity score" based on certain structural elements. Think of it as a Dungeon Master for your code, handing out XP based on how much chaos you’ve introduced.
The scoring system is based on a combination of Cyclomatic Complexity, Big O Notation—except, in true experimental fashion, it’s mostly arbitrary and meant for fun.

📌 **Current State**

- 🎯 It works! (But does it actually measure complexity? Debatable.)
- 🧮 Uses basic complexity metrics to assign a score.
- 🎲 Somewhat arbitrary rating system—because, let’s be honest, complexity is relative.
- 🛠 A work in progress—might get refined, or might just stay as a fun gimmick.

🧪 **Features (So Far)**

- ✅ Counts loops, conditionals, and function calls to determine script complexity.
- ✅ Assigns a "complexity score" based on weighted factors.
- ✅ Outputs a rating (e.g., "Beginner-friendly" vs. "Eldritch Horror of Spaghetti Code").
- ✅ Might accidentally roast your code—don’t take it personally.

💡 (Future enhancements include refining the scoring system, adding more metrics, and making it slightly less arbitrary.)

💡 **Why I Built This**

- 1️⃣ Because complexity metrics are interesting, even if they’re debatable.
- 2️⃣ Because I wanted a fun way to quantify "messy code."
- 3️⃣ Because I was curious about how tools like this work under the hood.

Like the sandbox, this project forced me to think differently about code—not just writing it, but analyzing its structure. Also, it gave me an excuse to experiment with abstract syntax trees (ASTs), recursion, and logic that sometimes hurts the brain.

📖 **How to Use the Analyzer**

- 📂 Check out code_analyzer.py—this is where the magic (or pseudo-magic) happens.
- 📊 Run it against a Python script to get a complexity score.
- 🎯 Laugh, cry, or debate the results—because complexity is subjective, after all.
- 🏆 Try writing a script to trick the analyzer—if you succeed, I salute you.


📌 **Notes & Future Plans**

- 🛠 Might tweak the scoring system—right now, it’s mostly logic, but a little bit of gut feeling.
- 🎭 Would be fun to integrate this into a game-like challenge—"Can you write the most unreadable Python script?"
- 🚀 Open to suggestions! If you have ideas on how to make the analysis more meaningful, feel free to contribute.
