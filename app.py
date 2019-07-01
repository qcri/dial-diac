from website import app


if __name__ == '__main__':
    # app.run(port=5000, host='0.0.0.0', debug=True, )
    # static_files just define a new set of paths for the application. you can use any of them later. it is good if your
    # static files are split in multiple places
    app.run(
        port=5000,
        host='0.0.0.0',
        debug=True,
        # static_files={'/demo/static': '/home/disooqi/projects/dial-diac/website/demo/static'},

    )
