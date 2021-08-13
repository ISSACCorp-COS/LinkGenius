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
            link.href = url;
            link.rel = "nofollow";
            link.target = "_blank";
            link.appendChild(url);
            document.body.appendChild(link);
        })();
    """
    replacements = [
        ("%PORT%", "%d" % port),
        ("%HEIGHT%", "%d" % height),
    ]
    for (k, v) in replacements:
        shell = shell.replace(k, v)

    return shell

