def create_iframe(port, height):
    # shell = """
    #     (async () => {
    #         const url = await google.colab.kernel.proxyPort(%PORT%, {"cache": true});
    #         console.log(`Adding iframe from URL:${url}`);
    #         const iframe = document.createElement('iframe');
    #         iframe.src = url;
    #         iframe.setAttribute('width', '100%');
    #         iframe.setAttribute('height', '%HEIGHT%');
    #         iframe.setAttribute('frameborder', 0);
    #         document.body.appendChild(iframe);
    #     })();
    # """
    shell = """
        (async () => {
            const url = await google.colab.kernel.proxyPort(%PORT%, {"cache": true});
            console.log(`Adding iframe from URL:${url}`);
            const link = document.createElement('a');
            link.setAttribute('href', url);
            link.setAttribute('rel', "nofollow");
            link.setAttribute('target', "_blank");
            link.text = url;
            document.body.appendChild(link);
            document.body.appendChild(url);
        })();
    """
    replacements = [
        ("%PORT%", "%d" % port),
        ("%HEIGHT%", "%d" % height),
    ]
    for (k, v) in replacements:
        shell = shell.replace(k, v)

    return shell

