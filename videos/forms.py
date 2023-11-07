from django.forms import ModelForm, Textarea,CheckboxSelectMultiple, ModelMultipleChoiceField, FileInput

from .models import Video, Comment, HashTag

class VideoForm(ModelForm):
    hashtags =ModelMultipleChoiceField(
                        queryset=HashTag.objects.all(),
                        widget=CheckboxSelectMultiple)
    class Meta:
        model = Video
        fields = ('name','description','video_file','hashtags') 
        widgets = {
            'video_file': FileInput(attrs={'accept': 'video/*'}),  
            'description': Textarea(attrs={'rows': 4, 'class': 'form-control'})
        }
        labels = {
            'video_file': 'Video Upload',  # Custom label for the video input field
        }
        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get('name')
            description = cleaned_data.get('description')
            video_file = cleaned_data.get('video_file')
            hashtags = cleaned_data.get('hashtags')

            if not name:
                self.add_error('name', 'Name is required.')

            if not description:
                self.add_error('description', 'Description is required.')

            if not video_file:
                self.add_error('video_file', 'Video file is required.')

            if not hashtags:
                self.add_error('hashtags', 'At least one hashtag is required.')

            return cleaned_data

class CommentsForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'aria-label': 'Comments',
                'placeholder': 'Add comment',
                'id': 'formComment',
                'rows': 3
            }),
        }