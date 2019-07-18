from datetime import datetime
from flask import render_template, request
from . import app, avi_vectorizer, avi_model
from .forms import DiacForm
from . import diacritization


@app.route('/demo/diacritization', methods=['GET', 'POST'])
def onmt_diacritizer():
    form = DiacForm()
    diac_out = ''
    dialect = ''
    if form.validate_on_submit():
        dialect_map = {'__label__DA-TN': 'tun', '__label__CA': 'ca', '__label__MSA': 'msa', '__label__DA-MA': 'mor'}
        if form.dialect.data == 'auto_detect':
            feature_vector = avi_vectorizer.transform([form.content.data])
            pred = avi_model.predict(feature_vector)
            dialect = dialect_map[pred[0]]
        else:
            dialect = form.dialect.data

        diac_out = diacritization.run_diac(form.content.data, dialect)
        # post = Post(title=form.title.data, content=form.content.data, author=current_user)

        # flash('Your sentence has been diacritized!', 'success')
        #return redirect(url_for('home'))
    # elif request.method == 'GET':
    #     raw_text = request.args.to_dict(flat=False).get('text', '')[0]
    #     dialect = request.args.to_dict(flat=False).get('d', 'ca')[0]
    #     diac_out = diacritization.run_diac(raw_text, dialect)

    dialect_label = {'':'Select A Variety', 'tun': 'Tunisian Dialect', 'ca': 'Classical Arabic',
                     'msa': 'Modern Standard Arabic', 'mor':'Moroccan Dialect'}
    return render_template('demos/onmt_diacritizer.html', title='New Sentence',
                           form=form, output=diac_out, final_dialect=dialect_label[dialect])


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}






