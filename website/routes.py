from datetime import datetime
from flask import render_template, request
from . import app
from .forms import DiacForm
from . import diacritization


@app.route('/demo/diacritization', methods=['GET', 'POST'])
def onmt_diacritizer():
    form = DiacForm()
    diac_out = ''
    if form.validate_on_submit():
        diac_out = diacritization.run_diac(form.content.data, form.dialect.data)
        # post = Post(title=form.title.data, content=form.content.data, author=current_user)

        # flash('Your sentence has been diacritized!', 'success')
        #return redirect(url_for('home'))
    elif request.method == 'GET':
        raw_text = request.args.to_dict(flat=False).get('text', '')[0]
        dialect = request.args.to_dict(flat=False).get('d', 'ca')[0]
        print(raw_text)
        diac_out = diacritization.run_diac(raw_text, dialect)

    return render_template('demos/onmt_diacritizer.html', title='New Sentence', form=form, output=diac_out)


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}






