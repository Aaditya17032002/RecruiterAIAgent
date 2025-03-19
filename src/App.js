import React from 'react';
import { BrowserRouter as Router, Routes, Route, Switch } from 'react-router-dom';
import { Box, Container } from '@mui/material';
import JobDescriptionInput from './components/JobDescriptionInput';
import ResumeUpload from './components/ResumeUpload';
import ResumeAnalysis from './components/ResumeAnalysis';
import { JobProvider } from './context/JobContext';
import JobScreeningResults from './components/JobScreeningResults';
import Navigation from './components/Navigation';
import AIInterviewScreen from './components/AIInterviewScreen';
import TempLoginPage from './components/TempLoginPage';

function App() {
    return (
        <JobProvider>
            <Router>
                <Box sx={{ minHeight: '100vh', bgcolor: '#f5f7fa' }}>
                    <Navigation />
                    <Container maxWidth="xl">
                        <Routes>
                            <Route path="/" element={<JobDescriptionInput />} />
                            <Route path="/upload" element={<ResumeUpload />} />
                            <Route path="/analysis" element={<ResumeAnalysis />} />
                            <Route path="/screening" element={<JobScreeningResults />} />
                            <Route path="/interview" element={<AIInterviewScreen />} />
                            <Route path="/temp-login" element={<TempLoginPage />} />
                        </Routes>
                    </Container>
                </Box>
            </Router>
        </JobProvider>
    );
}

export default App;
