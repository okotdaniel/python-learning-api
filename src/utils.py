
def upload_location(instance, filename):
    file_path = 'product/{product_name}/{filename}'.format(
        name=str(instance.first_name).split()[0], filename=filename)
    return file_path
