const pptxgen = require('pptxgenjs');
const path = require('path');

const html2pptx = require('./html2pptx.js');

async function createPresentation() {
    const pptx = new pptxgen();

    // Setup presentation properties
    pptx.layout = 'LAYOUT_16x9';
    pptx.title = 'KidsEnglish Fun - 融资汇报';
    pptx.author = 'KidsEnglish Fun Team';
    pptx.company = 'KidsEnglish Fun';
    pptx.subject = '幼儿英语学习游戏 Pre-Seed融资汇报';

    const slidesDir = path.join(__dirname, 'slides');

    // Slide files in order
    const slideFiles = [
        'slide1-title.html',
        'slide2-problem.html',
        'slide3-solution.html',
        'slide4-product.html',
        'slide5-tech.html',
        'slide6-market.html',
        'slide7-business.html',
        'slide8-roadmap.html',
        'slide9-ask.html',
        'slide10-contact.html'
    ];

    console.log('Creating presentation with', slideFiles.length, 'slides...\n');

    for (let i = 0; i < slideFiles.length; i++) {
        const slideFile = path.join(slidesDir, slideFiles[i]);
        console.log(`Processing slide ${i + 1}: ${slideFiles[i]}`);

        try {
            await html2pptx(slideFile, pptx);
            console.log(`  ✓ Slide ${i + 1} created successfully`);
        } catch (error) {
            console.error(`  ✗ Error creating slide ${i + 1}:`, error.message);
        }
    }

    // Save the presentation
    const outputPath = path.join(__dirname, '..', 'KidsEnglishFun-融资汇报.pptx');
    await pptx.writeFile({ fileName: outputPath });

    console.log('\n✓ Presentation saved to:', outputPath);
}

createPresentation().catch(err => {
    console.error('Failed to create presentation:', err);
    process.exit(1);
});
