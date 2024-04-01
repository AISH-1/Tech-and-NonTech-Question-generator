from flask import Flask, request, jsonify
import gemini


app = Flask(__name__)


@app.route('/generate_questions', methods=['POST'])
def generate_questions():
    data = request.get_json()

    resume_text = data.get('resume_text', '')
    job_description_text = data.get('job_description_text', '')
    skills = data.get('skills', [])

    custom_ntquestions = gemini.generate_custom_non_tech_questions(resume_text, job_description_text)
    custom_tquestions = gemini.generate_custom_tech_questions(", ".join(skills))

    result = {
        'custom_non_tech_questions': custom_ntquestions,
        'custom_tech_questions': custom_tquestions
    }
    
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
