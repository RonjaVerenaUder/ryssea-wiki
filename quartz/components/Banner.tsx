import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { resolveRelative } from "../util/path"

const Banner: QuartzComponent = ({ fileData, displayClass }: QuartzComponentProps) => {
  const banner = fileData.frontmatter?.banner as string | undefined
  if (!banner) return null

  const raw = banner.startsWith("http")
    ? banner
    : banner.startsWith("/")
      ? banner
      : `/${banner}`
  const src = raw.replace(/ /g, "-")

  return (
    <div class={`page-banner ${displayClass ?? ""}`}>
      <img src={src} alt="" />
    </div>
  )
}

Banner.css = `
.page-banner {
  width: 100vw;
  max-height: 150px;
  overflow: hidden;
}
.page-banner img {
  width: 100vw;
  height: 150px;
  object-fit: cover;
  object-position: center;
  display: block;
}
`

export default (() => Banner) satisfies QuartzComponentConstructor
