from django.shortcuts import redirect


def book_create(request):  # TODO: check how to create with CBV and use class methods for get data and DB search
    if request.method == 'GET':
        form = CreateBookForm()
        context = {
            'form': form
        }
        return render(request, 'book-create.html', context)
    else:
        try:
            autor_exist = Autors.objects.get(name=request.POST['autor'])
            autor = autor_exist
        except:
            autor = Autors.objects.create(name=request.POST[
                'autor'])  # TODO: validate(if author exist!?!?!) typo by user when populate form, make '.to_lower' and strip()

        try:
            publisher_exist = Publishers.objects.get(publisher_name=request.POST['publisher'])
            publisher = publisher_exist
        except:
            publisher = Publishers.objects.create(publisher_name=request.POST[
                'publisher'])  # TODO: validate(if author exist!?!?!) typo by user when populate form, make '.to_lower' and compare

        title = request.POST['title']
        description = request.POST['description']
        image1 = request.POST.get('image', False)  # get choosen image or set the default
        genre = request.POST['genre']
        owner = request.user
        year_of_publication = request.POST['year_of_publication']

        instance = Books(title=title, description=description, genre=genre, image=image1, owner=owner, autor=autor,
                         publisher=publisher,
                         year_of_publication=year_of_publication)  # , return_date=return_date, borrow_counter=borrow_counter)
        instance.save()

        return redirect('home page')
