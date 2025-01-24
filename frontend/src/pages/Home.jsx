import {useState, useEffect} from "react"
import api from "../api"
import "../styles/Home.css"
import Note from "../components/Note"
import SearchBar from "../components/SearchBar"

function Home(){
    const [notes, setNotes] = useState([])
    const [content, setContent] = useState ("")
    const [title, setTitle] = useState("")
    const [query, setQuery] = useState("")
    const [filteredNotes, setFilteredNotes] = useState([]); 
    
    useEffect(() => {
        getNotes();
    }, [])


    const getNotes = () => {
        api.get("/api/notes/")
            .then((res) => res.data)
            .then((data) => {
                setNotes(data);
                setFilteredNotes(data); // Initialize filteredNotes with all notes
            })
            .catch((err) => alert(err));
    };

    const deleteNote = (id) => {
        api.delete(`/api/notes/delete/${id}`).then((res)=> {
            if (res.status ===204) alert("Note deleted!")
                else alert("Failed to delete note.")
            getNotes();
        }).catch((error)=> alert(error));
    };

    const createNote = (e) => {
        e.preventDefault()
        api.post("/api/notes/", {content, title}).then((res) => {
            if (res.status ===201) alert("Note created!")
                else alert ("Failed to make note.")
            getNotes();
        }).catch((err)=> alert(err))
    };  

    const handleSearch = (searchQuery) => {
        setQuery(searchQuery); // Update the search query state

        if (searchQuery.trim() === "") {
            // Show all notes if the query is empty
            setFilteredNotes(notes);
        } else {
            // Filter notes based on the query
            const results = notes.filter((note) =>
                note.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                note.content.toLowerCase().includes(searchQuery.toLowerCase())
            );
            setFilteredNotes(results);
        }
    };

    return (
        <div>
            <h1>Notes</h1>

            {/* Search Bar */}
            <SearchBar onSearch={handleSearch} />

            {/* Display Notes */}
            <div>
                {filteredNotes.map((note) => (
                    <Note note={note} onDelete={deleteNote} key={note.id} />
                ))}
            </div>

            {/* Create Note Form */}
            <h2>Create a Note</h2>
            <form onSubmit={createNote}>
                <label htmlFor="title">Title:</label>
                <br />
                <input
                    type="text"
                    id="title"
                    name="title"
                    required
                    onChange={(e) => setTitle(e.target.value)}
                    value={title}
                />
                <br />
                <label htmlFor="content">Content:</label>
                <br />
                <textarea
                    id="content"
                    name="content"
                    required
                    onChange={(e) => setContent(e.target.value)}
                    value={content}
                ></textarea>
                <br />
                <input type="submit" value="Submit" />
            </form>
        </div>
    );


}

export default Home