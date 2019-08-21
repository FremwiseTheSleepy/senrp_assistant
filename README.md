
# How to Work It
Running:
  * Navigate to directory file is in within a command line
    * type *python rpg_assistant.py*
  * Output should be printed to command line in a somewhat readable fashion

Making modifications:
 * Open rpg_assistant.py in editor (recommend pycharm)
 * Navigate to bottom of page
    * Ctrl + end
 * Find *edit here* location after *__name__ == "__main__"* check
 * Make associated edits here or to the bad guy or weapon databases
    * weapon database should't need modifications since weapon modifiers are available, but could add new weapons 
    * bad guy database populated from books


# Planned Folder Structure
- Character
  - Sub-classes
  - Stat/Experience Tracking
- Interactions between Characters
  - Combat
    - Attack (hit status)
      - Attacker + Defender information
    - Attacker Calculates Damage
    - Defender Calculates Defense
- Render
- Configurations - with each item, such as HP, indicate how to place visually.
    
