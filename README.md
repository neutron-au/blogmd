![logo](https://github.com/neutron-au/blogmd/blob/main/logo.png?raw=true)
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
        blog/                         :  blog markdown page storage
            myproject/
                index.md              :  /blog/myproject/
                introduction/
                    index.md          :  /blog/myproject/introduction/
                    hello-world.md    :  /blog/myproject/introduction/hello-world/
                setup-examples/
                    index.md          :  /blog/myproject/setup-examples/
                    windows.md        :  /blog/myproject/setup-examples/windows/
                    linux.md          :  /blog/myproject/setup-examples/linux/
                    macos.md          :  /blog/myproject/setup-examples/macos/
        error/                        :  error response markdown page storage
        file/                         :  general file server files (css, images, html, etc)
    ...
```

To create new documentation pages, follow the above file structure. A given folder containing an index.md file (index of that folder) will take precedence over a markdown file with the same name as the folder if both within the same directory. e.g. `/blog/myproject/test/index.md` will take priority over `/blog/myproject/test.md`

Table showing the relatioship between markdown file and webserver view URL:

| File                                       | URL                                                     |
| ------------------------------------------ | ------------------------------------------------------- |
| `src/content/blog/myblog/index.md`         | `https://website.com/blog/myblog/`                      |
| `src/content/blog/myblog.md`               | `https://website.com/blog/myblog/`                      |
| `src/content/blog/myblog/hello-world.md`   | `https://website.com/blog/myblog/hello-world/`          |
| `src/content/blog/myblog/my-first-blog.md` | `https://website.com/blog/myblog/my-first-blog/`        |
