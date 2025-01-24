import React from "react";

function SearchBar({ onSearch }) {
    const handleInputChange = (e) => {
        onSearch(e.target.value); // Calls the parent function to handle search
    };

    return (
        <input

            type="text"
            placeholder="Filter Notes..."
            onChange={handleInputChange} // Trigger on every keystroke
        />
    );
}

export default SearchBar;
