# BlogMD
#### Neutron Australia

BlogMD is a simple REST API acting as a webserver, serving markdown files (.md) as webpages.

* Note: This project is new, and will be worked on in the background amongst the many private projects we have.


### Creating Documentation/Blogs
When the server starts it will create the default file structure:

```
src/
    main.py      
    content/    
        blog/      :  blog markdown page storage
        error/     :  error response markdown page storage
        file/      :  general file server files (css, images, html, etc)
    ...
```

To create new documentation pages, create folders and markdown (.md) files within the 'blog' directory. Once these have been created, they can be viewed by running the server, and entering in the path to that blog with the '.md' truncated.

Table showing the relatioship between markdown file and webserver view URL:

| Type | Data                                              |
| ---- | ------------------------------------------------- |
| File | `src/content/blog/myblog/my-first-blog.md`        |
| URL  | `https://website.com/blog/myblog/my-first-blog/`  |