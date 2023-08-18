
// Shiny tabs don't play nicely with anchor links, so this is some custom javascript to
// navigate to anchor links within another tab.
// Sources:
// https://davidruvolo51.github.io/shinytutorials/tutorials/internal-links-a/
// https://stackoverflow.com/questions/13735912/anchor-jumping-by-using-javascript
const customHref = function(link){

        const linkParts = link.split("#")
        let tab = linkParts[0]
        let anchor = linkParts[1]

        // find all links
        const links = document.getElementsByTagName("a");

        // since it returns an object, iterate over each entry
        Object.entries(links).forEach( (elem, i) => {

                // match data-value attribute with input var
                if(elem[1].getAttribute("data-value") === tab){

                        // if match, click link
                        elem[1].click();
                        document.getElementById(anchor).scrollIntoView();
                }
        });
}
