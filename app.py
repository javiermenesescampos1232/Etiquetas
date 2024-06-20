from flask import Flask, request, render_template, send_file
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

@app.route('/imp')
def index():
    return render_template('impresion.html')

@app.route('/generate-label', methods=['POST'])
def generate_label():
    school_name = request.form['school_name']
    student_name = request.form['student_name']
    student_id = request.form['student_id']
    student_course = request.form['student_course']
    admission_date = request.form['admission_date']
    school_logo = request.files['school_logo']
    
    label_width, label_height = 1200, 800
    label_image = Image.new('RGB', (label_width, label_height), color='white')
    draw = ImageDraw.Draw(label_image)

    # sirve  para mandar las iamgenes a nuestra etiquetas
    logo = Image.open(school_logo)
    logo = logo.resize((100, 100), Image.ANTIALIAS)
    
    logo_position = (label_width // 2 - 50, 20)
    label_image.paste(logo, logo_position)
    
    
    font = ImageFont.load_default()
    
    text_position = (label_width // 2 - draw.textsize(school_name, font=font)[0] // 2, 140)
    draw.text(text_position, school_name, fill='black', font=font)
    
    text_position = (label_width // 2 - draw.textsize(student_name, font=font)[0] // 2, 180)
    draw.text(text_position, student_name, fill='black', font=font)

    text_position = (label_width // 2 - draw.textsize(student_id, font=font)[0] // 2, 220)
    draw.text(text_position, student_id, fill='black', font=font)
    
    text_position = (label_width // 2 - draw.textsize(student_course, font=font)[0] // 2, 260)
    draw.text(text_position, student_course, fill='black', font=font)
    
    # Añadir la fecha de ingreso a la etiqueta
    text_position = (label_width // 2 - draw.textsize(admission_date, font=font)[0] // 2, 300)
    draw.text(text_position, admission_date, fill='black', font=font)
    
    # Guardar la imagen en un objeto BytesIO
    img_io = io.BytesIO()
    label_image.save(img_io, 'PNG')
    img_io.seek(0)
    
    # Enviar la imagen generada al navegador
    return send_file(img_io, mimetype='image/png', as_attachment=False, attachment_filename='label.png')

if __name__ == '__main__':
    app.run(debug=True)
