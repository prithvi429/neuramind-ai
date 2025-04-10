import React from "react";
import Header from "./components/Header";
import AgentCard from "./components/AgentCard";
import Footer from "./components/Footer";

function App() {
    return (
        <div>
            <Header />
            <main>
                <AgentCard />
            </main>
            <Footer />
        </div>
    );
}

export default App;
