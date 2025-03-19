# TalentFlow - AI-Powered Recruitment Platform

TalentFlow is a modern, AI-powered recruitment platform that streamlines the hiring process through intelligent candidate screening, automated interviews, and bias-free evaluation. Built with React and Material-UI, it offers a seamless experience for both recruiters and candidates.

![TalentFlow Logo](public/logo192.png)

## 🌟 Features

### 1. AI-Powered Interview System
- Real-time voice-based interviews
- Natural conversation flow with AI interviewer
- Automatic transcription and response analysis
- Dynamic question generation based on candidate responses

### 2. Resume Analysis
- Intelligent resume parsing
- Skill extraction and categorization
- Experience analysis
- Education and certification tracking

### 3. Job Description Analysis
- Automated job requirement extraction
- Skill matching and scoring
- Experience level assessment
- Role-specific criteria analysis

### 4. Candidate Screening
- Automated candidate evaluation
- Skill matching against job requirements
- Experience relevance scoring
- Bias mitigation in evaluation

### 5. Modern UI/UX
- Clean and intuitive interface
- Real-time voice animations
- Progress tracking
- Responsive design for all devices

## 🚀 Getting Started

### Prerequisites
- Node.js (v14 or higher)
- npm or yarn package manager
- Modern web browser with microphone support

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Aaditya17032002/RecruiterAIAgent.git
cd RecruiterAIAgent
```

2. Install dependencies:
```bash
npm install
# or
yarn install
```

3. Start the development server:
```bash
npm start
# or
yarn start
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## 📁 Project Structure

```
src/
├── components/           # React components
│   ├── AIInterviewScreen.js    # AI interview interface
│   ├── ResumeUpload.js         # Resume upload component
│   ├── JobDescriptionInput.js  # Job posting creation
│   ├── CandidateScreening.js   # Candidate evaluation
│   └── ...                     # Other UI components
├── services/            # API and service integrations
├── context/            # React context providers
├── utils/              # Utility functions
└── data/               # Static data and constants
```

## 🔄 Application Flow

1. **Job Description Creation**
   - Recruiter creates a job posting
   - System analyzes requirements and skills

2. **Resume Upload & Analysis**
   - Candidates upload their resumes
   - System extracts and categorizes information

3. **Candidate Screening**
   - Automated evaluation of candidates
   - Skill matching and scoring
   - Bias-free assessment

4. **AI Interview**
   - Voice-based interview with AI
   - Real-time transcription
   - Dynamic question generation
   - Response analysis

5. **Results & Evaluation**
   - Comprehensive candidate assessment
   - Detailed matching report
   - Final scoring and recommendations

## 🛠️ Technologies Used

- **Frontend Framework**: React 19
- **UI Library**: Material-UI
- **Animations**: Framer Motion
- **Routing**: React Router
- **State Management**: React Context
- **API Integration**: Axios
- **File Handling**: React Dropzone
- **PDF Processing**: PDF.js

## 🔧 Configuration

The application uses environment variables for configuration. Create a `.env` file in the root directory:

```env
REACT_APP_API_URL=your_api_url
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Aaditya** - *Initial work* - [Aaditya17032002](https://github.com/Aaditya17032002)

## 🙏 Acknowledgments

- Material-UI for the beautiful components
- Framer Motion for smooth animations
- React community for excellent tools and libraries

## 📞 Support

For support, email support@talentflow.com or create an issue in the repository.

---

Made with ❤️ by the TalentFlow Team
