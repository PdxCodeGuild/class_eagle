class ChecklistForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields= ("done")

    def save(self, todo=None):
        todo = super(ChecklistForm, self).save(commit=False)

        if name:
            Todo.name = name
        todo.save()
        return todo
